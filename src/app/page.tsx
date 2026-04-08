import React from 'react';
import { BookOpen, Code, BrainCircuit } from 'lucide-react';

export default function Home() {
  return (
    <div style={{ padding: '2rem 0' }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Welcome to Youngjin's TIL Garden 🌱</h1>
      <p style={{ fontSize: '1.2rem', color: 'var(--secondary)', marginBottom: '3rem' }}>
        기록은 기억을 지배한다. 매일의 배움을 소중하게 담아내는 공간입니다.
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem' }}>
        <div style={{ padding: '2rem', border: '1px solid var(--sidebar-border)', borderRadius: 'var(--border-radius)', background: '#fcfcfc' }}>
          <BrainCircuit size={40} color="var(--primary)" style={{ marginBottom: '1rem' }} />
          <h3>AI Lab</h3>
          <p>Deep Learning, Generative Models, and NLP studies.</p>
        </div>
        <div style={{ padding: '2rem', border: '1px solid var(--sidebar-border)', borderRadius: 'var(--border-radius)', background: '#fcfcfc' }}>
          <Code size={40} color="#22c55e" style={{ marginBottom: '1rem' }} />
          <h3>Coding Test</h3>
          <p>Algorithm problem solving and data structures.</p>
        </div>
        <div style={{ padding: '2rem', border: '1px solid var(--sidebar-border)', borderRadius: 'var(--border-radius)', background: '#fcfcfc' }}>
          <BookOpen size={40} color="#f59e0b" style={{ marginBottom: '1rem' }} />
          <h3>Knowledge Base</h3>
          <p>System architecture and software engineering principles.</p>
        </div>
      </div>
    </div>
  );
}
