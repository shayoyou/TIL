import React from 'react';
import { MarkdownRenderer } from './MarkdownRenderer';
import styles from './NotebookRenderer.module.css';

interface NotebookCell {
  cell_type: 'markdown' | 'code';
  source: string | string[];
  outputs?: any[];
  execution_count?: number;
}

interface NotebookData {
  cells: NotebookCell[];
}

interface NotebookRendererProps {
  data: NotebookData;
}

const formatSource = (source: string | string[]) => {
  if (Array.isArray(source)) {
    return source.join('');
  }
  return source;
};

export const NotebookRenderer: React.FC<NotebookRendererProps> = ({ data }) => {
  return (
    <div className={styles.notebook}>
      {data.cells.map((cell, index) => (
        <div key={index} className={styles.cell}>
          {cell.cell_type === 'markdown' ? (
            <div className={styles.markdownCell}>
              <MarkdownRenderer content={formatSource(cell.source)} />
            </div>
          ) : (
            <div className={styles.codeCell}>
              <div className={styles.inputArea}>
                <div className={styles.prompt}>In [{cell.execution_count || ' '}]:</div>
                <div className={styles.code}>
                  <pre>
                    <code>{formatSource(cell.source)}</code>
                  </pre>
                </div>
              </div>
              {cell.outputs && cell.outputs.length > 0 && (
                <div className={styles.outputArea}>
                  <div className={styles.prompt}>Out [{cell.execution_count || ' '}]:</div>
                  <div className={styles.output}>
                    {cell.outputs.map((output, outIdx) => (
                      <div key={outIdx}>
                        {output.name === 'stdout' && <pre>{formatSource(output.text)}</pre>}
                        {output.data && output.data['text/plain'] && (
                          <pre>{formatSource(output.data['text/plain'])}</pre>
                        )}
                        {output.data && output.data['image/png'] && (
                          <img src={`data:image/png;base64,${output.data['image/png']}`} alt="Output" />
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};
