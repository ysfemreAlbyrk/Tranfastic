<section class="download section">
  <div class="container">
    <div class="section-header mb-20">
      <h2 class="section-title mb-6">Ready to get started?</h2>
      <p class="section-description">Download Tranfastic and start translating instantly</p>
    </div>
    
    <div class="download-content">
      <div class="main-download">
        <div class="download-card primary-card glass">
          <div class="download-visual mb-8">
            <div class="download-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                <path d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z"/>
              </svg>
            </div>
          </div>
          
          <h3 class="download-title mb-4">Download for Windows</h3>
          <p class="download-description mb-8">Portable executable - no installation required</p>
          
          <a href="https://github.com/ysfemreAlbyrk/Tranfastic/releases/latest" 
             class="btn btn-primary btn-large download-btn" 
             target="_blank" 
             rel="noopener noreferrer">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z"/>
            </svg>
            Download Tranfastic.exe
          </a>
          
          <div class="download-meta mt-6">
            <div class="meta-item">
              <span class="meta-label">Size:</span>
              <span class="meta-value">~45MB</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Platform:</span>
              <span class="meta-value">Windows 10/11</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">License:</span>
              <span class="meta-value">MIT</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="secondary-options">
        <div class="option-card glass">
          <h4 class="option-title mb-4">🛠️ For Developers</h4>
          <p class="option-description mb-6">Build from source or contribute</p>
          
          <div class="option-buttons">
            <a href="https://github.com/ysfemreAlbyrk/Tranfastic" 
               class="btn btn-secondary" 
               target="_blank" 
               rel="noopener noreferrer">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
              </svg>
              View Source
            </a>
            
            <a href="https://github.com/ysfemreAlbyrk/Tranfastic/releases" 
               class="btn btn-secondary" 
               target="_blank" 
               rel="noopener noreferrer">
              All Releases
            </a>
          </div>
        </div>
        
        <div class="requirements-card glass">
          <h4 class="requirements-title mb-4">📋 Requirements</h4>
          <ul class="requirements-list">
            <li>Windows 10 or later</li>
            <li>64-bit architecture</li>
            <li>10MB free space</li>
            <li>Internet connection</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .download {
    background: var(--bg-secondary);
    position: relative;
  }
  
  .download::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 70% 30%, rgba(139, 92, 246, 0.05) 0%, transparent 60%);
    pointer-events: none;
  }
  
  .section-header {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
  }
  
  .section-title {
    color: var(--text-primary);
    font-weight: 700;
    line-height: 1.2;
  }
  
  .section-description {
    font-size: var(--text-xl);
    color: var(--text-secondary);
    margin: 0;
  }
  
  .download-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: var(--space-8);
    align-items: start;
    position: relative;
    z-index: 1;
  }
  
  .download-card {
    padding: var(--space-12);
    border-radius: var(--radius-3xl);
    text-align: center;
    border: 1px solid var(--border);
  }
  
  .primary-card {
    border: 2px solid var(--primary-light);
    background: linear-gradient(135deg, var(--bg-glass) 0%, rgba(99, 102, 241, 0.05) 100%);
  }
  
  .download-visual {
    display: flex;
    justify-content: center;
  }
  
  .download-icon {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: var(--shadow-glow);
  }
  
  .download-title {
    color: var(--text-primary);
    font-size: var(--text-2xl);
    font-weight: 600;
    margin: 0;
  }
  
  .download-description {
    color: var(--text-secondary);
    margin: 0;
  }
  
  .download-btn {
    width: 100%;
    max-width: 300px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  }
  
  .download-meta {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }
  
  .meta-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--space-2) var(--space-4);
    background: var(--bg-glass);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
  }
  
  .meta-label {
    font-size: var(--text-sm);
    color: var(--text-muted);
  }
  
  .meta-value {
    font-size: var(--text-sm);
    color: var(--text-primary);
    font-weight: 500;
  }
  
  .secondary-options {
    display: flex;
    flex-direction: column;
    gap: var(--space-6);
  }
  
  .option-card, .requirements-card {
    padding: var(--space-8);
    border-radius: var(--radius-2xl);
    border: 1px solid var(--border);
  }
  
  .option-title, .requirements-title {
    color: var(--text-primary);
    font-size: var(--text-lg);
    font-weight: 600;
    margin: 0;
  }
  
  .option-description {
    color: var(--text-secondary);
    font-size: var(--text-base);
    margin: 0;
  }
  
  .option-buttons {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }
  
  .requirements-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  .requirements-list li {
    padding: var(--space-2) 0;
    color: var(--text-secondary);
    font-size: var(--text-sm);
    position: relative;
    padding-left: var(--space-6);
  }
  
  .requirements-list li::before {
    content: '✓';
    color: var(--success);
    font-weight: bold;
    position: absolute;
    left: 0;
    top: var(--space-2);
  }
  
  @media (max-width: 1024px) {
    .download-content {
      grid-template-columns: 1fr;
      gap: var(--space-12);
    }
  }
  
  @media (max-width: 768px) {
    .download-card {
      padding: var(--space-8);
    }
    
    .download-icon {
      width: 80px;
      height: 80px;
    }
    
    .download-icon svg {
      width: 36px;
      height: 36px;
    }
    
    .secondary-options {
      gap: var(--space-4);
    }
    
    .option-card, .requirements-card {
      padding: var(--space-6);
    }
  }
</style> 