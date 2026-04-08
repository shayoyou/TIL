import React from 'react';
import { getFileContent, getContentTree } from '@/lib/content';
import { MarkdownRenderer } from '@/components/MarkdownRenderer';
import { NotebookRenderer } from '@/components/NotebookRenderer';
import { notFound } from 'next/navigation';

interface PageProps {
  params: {
    slug: string[];
  };
}

export async function generateStaticParams() {
  const tree = getContentTree();
  const paths: { slug: string[] }[] = [];

  const walk = (nodes: any[]) => {
    nodes.forEach((node) => {
      if (node.type === 'file') {
        paths.push({
          slug: node.path.split(/[/\\]/).filter(Boolean),
        });
      } else if (node.children) {
        walk(node.children);
      }
    });
  };

  walk(tree);
  return paths;
}

export default async function ContentPage({ params }: PageProps) {
  const filePath = decodeURIComponent(params.slug.join('/'));
  
  try {
    const { type, metadata, content } = await getFileContent(filePath);

    let displayContent = content;
    if (type === 'code') {
      displayContent = `\`\`\`${metadata.language}\n${content}\n\`\`\``;
    }

    return (
      <div>
        <header style={{ marginBottom: '3rem', borderBottom: '1px solid var(--sidebar-border)', paddingBottom: '1rem' }}>
          <div style={{ color: 'var(--secondary)', fontSize: '0.9rem', marginBottom: '0.5rem' }}>
            {params.slug.slice(0, -1).join(' / ')}
          </div>
          <h1 style={{ marginTop: 0 }}>{metadata.title}</h1>
          {metadata.date && (
            <div style={{ fontSize: '0.85rem', color: '#999' }}>{metadata.date}</div>
          )}
        </header>

        {type === 'markdown' || type === 'code' ? (
          <MarkdownRenderer content={displayContent as string} />
        ) : (
          <NotebookRenderer data={content as any} />
        )}
      </div>
    );
  } catch (error) {
    console.error(error);
    return notFound();
  }
}
