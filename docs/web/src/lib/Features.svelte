<section class="features section">
  <div class="container">
    <div class="section-header mb-20">
      <h2 class="section-title mb-6">Everything you need for instant translation</h2>
      <p class="section-description">Powerful features designed for seamless workflow integration</p>
    </div>
    
    <div class="features-grid">
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">🔥</div>
          <h3>Instant Translation</h3>
        </div>
        <p>Quick translate with global hotkey (Shift+Alt+D). No waiting, no interruptions to your workflow.</p>
      </div>
      
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">⚡</div>
          <h3>Hotkey Activation</h3>
        </div>
        <p>Opens translation popup instantly with a customizable keyboard shortcut. Work faster than ever before.</p>
      </div>
      
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">🌐</div>
          <h3>Multiple Languages</h3>
        </div>
        <p>Support for English, Turkish, German, Spanish, Japanese and more with automatic language detection.</p>
      </div>
      
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">📱</div>
          <h3>System Tray</h3>
        </div>
        <p>Runs quietly in the background. Stays out of your way until you need it.</p>
      </div>
      
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">📋</div>
          <h3>Clipboard Integration</h3>
        </div>
        <p>Automatic paste translated text where you need it. Seamless workflow integration.</p>
      </div>
      
      <div class="feature-card glass">
        <div class="feature-header mb-6">
          <div class="feature-icon">🔒</div>
          <h3>Privacy Focused</h3>
        </div>
        <p>Does not store any translation history or sensitive information. Your data stays private.</p>
      </div>
    </div>
  </div>
</section>

<style>
  .features {
    background: var(--bg-secondary);
    position: relative;
  }
  
  .features::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 50%, rgba(99, 102, 241, 0.03) 0%, transparent 70%);
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
  
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: var(--space-8);
    position: relative;
    z-index: 1;
  }
  
  .feature-card {
    padding: var(--space-8);
    border-radius: var(--radius-2xl);
    transition: all 0.4s ease;
    position: relative;
    border: 1px solid var(--border);
  }
  
  .feature-card:hover {
    transform: translateY(-8px);
    border-color: var(--primary-light);
    box-shadow: var(--shadow-xl);
  }
  
  .feature-header {
    display: flex;
    align-items: center;
    gap: var(--space-4);
  }
  
  .feature-icon {
    font-size: var(--text-3xl);
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-glass);
    border-radius: var(--radius-xl);
    border: 1px solid var(--border);
    backdrop-filter: blur(20px);
  }
  
  .feature-card h3 {
    color: var(--text-primary);
    font-size: var(--text-xl);
    font-weight: 600;
    margin: 0;
  }
  
  .feature-card p {
    font-size: var(--text-base);
    line-height: 1.6;
    color: var(--text-secondary);
    margin: 0;
  }
  
  @media (max-width: 768px) {
    .features-grid {
      grid-template-columns: 1fr;
      gap: var(--space-6);
    }
    
    .feature-card {
      padding: var(--space-6);
    }
    
    .feature-header {
      flex-direction: column;
      text-align: center;
      gap: var(--space-3);
    }
    
    .feature-icon {
      width: 50px;
      height: 50px;
      font-size: var(--text-2xl);
    }
  }
</style> 