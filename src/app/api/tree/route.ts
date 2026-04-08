import { getContentTree } from '@/lib/content';
import { NextResponse } from 'next/server';

export async function GET() {
  const tree = getContentTree();
  return NextResponse.json(tree);
}
