import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import '@/styles/globals.css';
import { Sidebar } from '@/components/Sidebar';
import { getContentTree } from '@/lib/content';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: "Youngjin's TIL Garden",
  description: "Personal Today I Learned platform for Youngjin",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const tree = getContentTree();

  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="container">
          <Sidebar tree={tree} />
          <main className="main-content">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
