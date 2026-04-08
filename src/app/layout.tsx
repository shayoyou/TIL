"use client";

import React, { useState, useEffect } from 'react';
import { Inter } from 'next/font/google';
import '@/styles/globals.css';
import { Sidebar } from '@/components/Sidebar';
import { ContentNode } from '@/lib/content';
import { Menu, X } from 'lucide-react';
import { usePathname } from 'next/navigation';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [tree, setTree] = useState<ContentNode[]>([]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const pathname = usePathname();

  // Close sidebar when route changes on mobile
  useEffect(() => {
    setIsSidebarOpen(false);
  }, [pathname]);

  // Fetch tree data on client
  useEffect(() => {
    const fetchTree = async () => {
      try {
        const res = await fetch('/api/tree');
        const data = await res.json();
        setTree(data);
      } catch (err) {
        console.error('Failed to fetch tree:', err);
      }
    };
    fetchTree();
  }, []);

  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="container">
          {/* Mobile Header */}
          <header className="mobile-header">
            <button className="menu-toggle" onClick={() => setIsSidebarOpen(!isSidebarOpen)}>
              {isSidebarOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
            <div className="mobile-logo">Youngjin's TIL</div>
          </header>

          <div className={`sidebar-wrapper ${isSidebarOpen ? 'open' : ''}`}>
             <Sidebar tree={tree} />
          </div>
          
          {/* Overlay for mobile */}
          {isSidebarOpen && <div className="sidebar-overlay" onClick={() => setIsSidebarOpen(false)} />}

          <main className="main-content">
            {children}
          </main>
        </div>

        <style jsx global>{`
          .mobile-header {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: var(--header-height);
            background: var(--background);
            border-bottom: 1px solid var(--sidebar-border);
            z-index: 100;
            padding: 0 1rem;
            align-items: center;
          }

          .menu-toggle {
            background: none;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
            color: var(--foreground);
          }

          .mobile-logo {
            margin-left: 1rem;
            font-weight: 800;
            color: var(--primary);
          }

          .sidebar-wrapper {
            transition: transform 0.3s ease;
          }

          @media (max-width: 768px) {
            .mobile-header {
              display: flex;
            }

            .sidebar-wrapper {
              position: fixed;
              top: var(--header-height);
              left: 0;
              bottom: 0;
              z-index: 101;
              transform: translateX(-100%);
              background: var(--sidebar-bg);
              width: 280px;
              box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            }

            .sidebar-wrapper.open {
              transform: translateX(0);
            }

            .sidebar-overlay {
              position: fixed;
              top: 0;
              left: 0;
              right: 0;
              bottom: 0;
              background: rgba(0,0,0,0.5);
              z-index: 99;
            }
          }
        `}</style>
      </body>
    </html>
  );
}
