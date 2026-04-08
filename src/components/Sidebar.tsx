"use client";

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { ContentNode } from '@/lib/content';
import styles from './Sidebar.module.css';
import { Folder, FileText, ChevronRight, ChevronDown } from 'lucide-react';
import { clsx } from 'clsx';

interface SidebarProps {
  tree: ContentNode[];
}

const SidebarItem: React.FC<{ node: ContentNode; depth: number }> = ({ node, depth }) => {
  const pathname = usePathname();
  const nodePath = `/${node.path.replace(/\\/g, '/')}`;
  const isChildActive = pathname.startsWith(nodePath);
  const [isOpen, setIsOpen] = React.useState(isChildActive);
  const isActive = pathname === nodePath;

  const toggleOpen = (e: React.MouseEvent) => {
    if (node.type === 'directory') {
      e.preventDefault();
      setIsOpen(!isOpen);
    }
  };

  const Icon = node.type === 'directory' ? (isOpen ? ChevronDown : ChevronRight) : FileText;

  return (
    <div className={styles.itemWrapper}>
      <div 
        className={clsx(styles.item, isActive && styles.active)}
        style={{ paddingLeft: `${depth * 1.2}rem` }}
      >
        {node.type === 'directory' ? (
          <div className={styles.dirHeader} onClick={toggleOpen}>
            <Icon size={16} className={styles.icon} />
            <Folder size={18} className={styles.folderIcon} />
            <span>{node.name}</span>
          </div>
        ) : (
          <Link href={`/${node.path.replace(/\\/g, '/')}`} className={styles.fileLink}>
            <FileText size={16} className={styles.fileIcon} />
            <span>{node.name.replace(/\.(md|ipynb)$/, '')}</span>
          </Link>
        )}
      </div>
      {node.type === 'directory' && isOpen && node.children && (
        <div className={styles.children}>
          {node.children.map((child) => (
            <SidebarItem key={child.path} node={child} depth={depth + 1} />
          ))}
        </div>
      )}
    </div>
  );
};

export const Sidebar: React.FC<SidebarProps> = ({ tree }) => {
  return (
    <aside className={styles.sidebar}>
      <div className={styles.logo}>
        <Link href="/">
          <h1>Youngjin's TIL</h1>
        </Link>
      </div>
      <nav className={styles.nav}>
        {tree.map((node) => (
          <SidebarItem key={node.path} node={node} depth={0} />
        ))}
      </nav>
    </aside>
  );
};
