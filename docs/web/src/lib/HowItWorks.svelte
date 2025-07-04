<section class="how-it-works section">
  <div class="container">
    <div class="section-header mb-20">
      <h2 class="section-title mb-6">How it works</h2>
      <p class="section-description">Get started in seconds with these simple steps</p>
    </div>
    
    <div class="steps-wrapper">
      <div class="step-item">
        <div class="step-content">
          <div class="step-number">01</div>
          <div class="step-info">
            <h3 class="step-title">Download & Run</h3>
            <p class="step-text">Download Tranfastic.exe and double-click to run. The app will appear in your system tray.</p>
          </div>
        </div>
        <div class="step-visual">
          <div class="step-icon">📥</div>
        </div>
      </div>
      
      <div class="step-item reverse">
        <div class="step-visual">
          <div class="step-icon">⌨️</div>
        </div>
        <div class="step-content">
          <div class="step-number">02</div>
          <div class="step-info">
            <h3 class="step-title">Press Hotkey</h3>
            <p class="step-text">Press <kbd>Shift+Alt+D</kbd> (or your custom hotkey) to open the translation window.</p>
          </div>
        </div>
      </div>
      
      <div class="step-item">
        <div class="step-content">
          <div class="step-number">03</div>
          <div class="step-info">
            <h3 class="step-title">Type & Translate</h3>
            <p class="step-text">Type or paste your text and press <kbd>Enter</kbd> to get instant translation.</p>
          </div>
        </div>
        <div class="step-visual">
          <div class="step-icon">✨</div>
        </div>
      </div>
      
      <div class="step-item reverse">
        <div class="step-visual">
          <div class="step-icon">🎯</div>
        </div>
        <div class="step-content">
          <div class="step-number">04</div>
          <div class="step-info">
            <h3 class="step-title">Auto Paste</h3>
            <p class="step-text">The translated text is automatically pasted where you need it. Press <kbd>Esc</kbd> to close.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .how-it-works {
    background: var(--bg-primary);
    position: relative;
  }
  
  .section-header {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
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
  
  .steps-wrapper {
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-8);
  }
  
  .step-item {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--space-12);
    align-items: center;
    position: relative;
    border-top: 1px solid var(--border);
    padding-top: var(--space-6);
    transition: all 0.3s ease;
  }
  
  .step-item:hover {
    filter: drop-shadow(0 0 10px var(--primary-light));
  }

  .step-item.reverse {
    grid-template-columns: auto 1fr;
  }
  
  .step-item.reverse .step-content {
    text-align: right;
  }
  
  .step-content {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
  }
  
  .step-number {
    font-size: var(--text-sm);
    font-weight: 700;
    color: var(--primary-light);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }
  
  .step-title {
    font-size: var(--text-2xl);
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
    line-height: 1.3;
  }
  
  .step-text {
    font-size: var(--text-base);
    color: var(--text-secondary);
    line-height: 1.6;
    margin: 0;
    max-width: 400px;
  }
  
  .step-visual {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .step-icon {
    width: 120px;
    height: 120px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--text-4xl);
    backdrop-filter: blur(20px);
    transition: all 0.3s ease;
  }
  
  kbd {
    background: var(--bg-glass);
    color: var(--text-accent);
    padding: var(--space-1) var(--space-2);
    border-radius: var(--radius-sm);
    font-size: var(--text-sm);
    border: 1px solid var(--border);
    font-family: monospace;
    font-weight: 500;
  }
  
  .workflow-summary {
    display: flex;
    justify-content: center;
  }
  
  .summary-card {
    padding: var(--space-8);
    border-radius: var(--radius-2xl);
    max-width: 500px;
    width: 100%;
    text-align: center;
    border: 1px solid var(--border);
  }
  
  .summary-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--space-3);
  }
  
  .summary-icon {
    font-size: var(--text-2xl);
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .summary-title {
    color: var(--text-primary);
    font-weight: 600;
    margin: 0;
    font-size: var(--text-xl);
  }
  
  .summary-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--space-4);
    flex-wrap: wrap;
  }
  
  .flow-step {
    background: var(--bg-glass);
    color: var(--text-primary);
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-lg);
    font-size: var(--text-sm);
    font-weight: 500;
    border: 1px solid var(--border);
    backdrop-filter: blur(20px);
  }
  
  .flow-arrow {
    color: var(--primary-light);
    font-size: var(--text-lg);
    font-weight: bold;
  }
  
  @media (max-width: 768px) {
    .steps-wrapper {
      gap: var(--space-12);
    }
    
    .step-item,
    .step-item.reverse {
      grid-template-columns: 1fr;
      text-align: center;
      gap: var(--space-6);
    }
    
    .step-item.reverse .step-content {
      text-align: center;
    }
    
    .step-icon {
      width: 80px;
      height: 80px;
      font-size: var(--text-2xl);
    }
    
    .step-text {
      max-width: none;
    }
    
    .summary-flow {
      flex-direction: column;
      gap: var(--space-2);
    }
    
    .flow-arrow {
      transform: rotate(90deg);
    }
  }
</style> 