import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const CONTENT_DIRS = ['ai_lab', 'coding_test'];

export interface ContentNode {
  name: string;
  path: string;
  type: 'file' | 'directory';
  children?: ContentNode[];
}

export interface ContentMetadata {
  title: string;
  date?: string;
  tags?: string[];
  [key: string]: any;
}

export const getContentTree = (): ContentNode[] => {
  const buildTree = (dir: string, base: string = ''): ContentNode[] => {
    const fullPath = path.join(process.cwd(), dir);
    const entries = fs.readdirSync(fullPath, { withFileTypes: true });

    return entries
      .filter((entry) => !entry.name.startsWith('.') && entry.name !== 'node_modules' && entry.name !== 'src')
      .map((entry) => {
        const relativePath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
          return {
            name: entry.name,
            path: relativePath,
            type: 'directory',
            children: buildTree(relativePath),
          };
        }
        return {
          name: entry.name,
          path: relativePath,
          type: 'file',
        };
      })
      .filter((node) => 
        node.type === 'directory' || 
        node.name.endsWith('.md') || 
        node.name.endsWith('.ipynb') ||
        /\.(py|cpp|js|ts|java|c|h|cs|go|rs|rb|php)$/.test(node.name)
      );
  };

  return CONTENT_DIRS.map((dir) => ({
    name: dir === 'ai_lab' ? 'AI Lab' : 'Coding Test',
    path: dir,
    type: 'directory',
    children: buildTree(dir),
  }));
};

export const getFileContent = async (filePath: string) => {
  const fullPath = path.join(process.cwd(), filePath);
  const fileContent = fs.readFileSync(fullPath, 'utf8');

  if (filePath.endsWith('.md')) {
    const { data, content } = matter(fileContent);
    return {
      type: 'markdown',
      metadata: {
        title: data.title || path.basename(filePath, '.md'),
        ...data,
      } as ContentMetadata,
      content,
    };
  }

  if (filePath.endsWith('.ipynb')) {
    const notebook = JSON.parse(fileContent);
    return {
      type: 'notebook',
      metadata: {
        title: path.basename(filePath, '.ipynb'),
      } as ContentMetadata,
      content: notebook,
    };
  }

  // Handle source code files
  const codeExtMatch = filePath.match(/\.(py|cpp|js|ts|java|c|h|cs|go|rs|rb|php)$/);
  if (codeExtMatch) {
    const ext = codeExtMatch[1];
    return {
      type: 'code',
      metadata: {
        title: path.basename(filePath),
        language: ext === 'py' ? 'python' : ext === 'cpp' ? 'cpp' : ext,
      } as ContentMetadata,
      content: fileContent,
    };
  }

  throw new Error('Unsupported file type');
};
