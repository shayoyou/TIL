import Link from 'next/link';

export default function NotFound() {
  return (
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center', 
      justifyContent: 'center', 
      height: '60vh',
      textAlign: 'center'
    }}>
      <h2 style={{ fontSize: '3rem', marginBottom: '1rem' }}>404</h2>
      <p style={{ fontSize: '1.2rem', color: 'var(--secondary)', marginBottom: '2rem' }}>
        오빠, 이 문서는 아직 제 정원에 심어지지 않은 것 같아요! 🌿
      </p>
      <Link href="/" style={{ 
        padding: '0.8rem 1.5rem', 
        background: 'var(--primary)', 
        color: 'white', 
        borderRadius: 'var(--border-radius)',
        fontWeight: '600'
      }}>
        홈으로 돌아가기
      </Link>
    </div>
  );
}
