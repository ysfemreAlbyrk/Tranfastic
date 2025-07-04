<script>
  import { onMount } from 'svelte';
  
  let heroSection;
  
  onMount(() => {
    if (heroSection) {
      heroSection.classList.add('fade-in-up');
    }
  });
</script>

<section class="hero" bind:this={heroSection}>
  <div class="hero-bg">
    <div class="bg-gradient-1"></div>
    <div class="bg-gradient-2"></div>
  </div>
  
  <div class="container">
    <div class="hero-content">
      <div class="hero-icon mb-8 float">
        <img src="/icon.png" alt="Tranfastic Icon" class="app-icon" />
      </div>
      
      <h1 class="hero-title mb-6">
        <span class="text-gradient">Tranfastic</span>
      </h1>
      
      <p class="hero-subtitle mb-8">
        Lightweight Portable Instant Translator App
      </p>
      
      <p class="hero-description mb-12">
        Instant, real-time translation while you work. A quick hotkey opens a translation window, making translated text readily available for copying or inserting.
      </p>
      
      <div class="hero-actions mb-16">
        <a href="https://github.com/ysfemreAlbyrk/Tranfastic/releases/latest" 
           class="btn btn-primary btn-large download-btn" 
           target="_blank" 
           rel="noopener noreferrer">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z"/>
          </svg>
          Download for Windows
        </a>
        
        <a href="https://github.com/ysfemreAlbyrk/Tranfastic" 
           class="btn btn-secondary btn-large" 
           target="_blank" 
           rel="noopener noreferrer">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
          </svg>
          View Source
        </a>
      </div>
      
      <div class="hero-stats">
        <div class="stat">
          <span class="stat-icon">🚀</span>
          <span class="stat-text">Instant Start</span>
        </div>
        <div class="stat">
          <span class="stat-icon">🔒</span>
          <span class="stat-text">Privacy First</span>
        </div>
        <div class="stat">
          <span class="stat-icon">📦</span>
          <span class="stat-text">No Installation</span>
        </div>
        <div class="stat">
          <span class="stat-icon">⚡</span>
          <span class="stat-text">5MB Only</span>
        </div>
      </div>
    </div>
    
    <div class="hero-visual">
      <div class="app-preview">
        <img src="/app.png" alt="Tranfastic App Screenshot" class="app-screenshot" />
        <div class="preview-overlay"></div>
      </div>
    </div>
  </div>
</section>

<style>
  .hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    padding: var(--space-20) 0;
  }
  
  .hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    overflow: hidden;
  }
  
  .bg-gradient-1 {
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.1) 0%, transparent 50%);
    animation: float 6s ease-in-out infinite;
  }
  
  .bg-gradient-2 {
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.08) 0%, transparent 50%);
    animation: float 8s ease-in-out infinite reverse;
  }
  
  .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-20);
    align-items: center;
    position: relative;
    z-index: 1;
  }
  
  .hero-content {
    max-width: 600px;
  }
  
  .hero-icon {
    display: flex;
    justify-content: flex-start;
  }
  
  .app-icon {
    width: 100px;
    height: 100px;
    border-radius: var(--radius-3xl);
    box-shadow: var(--shadow-xl);
    background: var(--bg-glass);
    padding: var(--space-2);
    border: 1px solid var(--border);
  }
  
  .hero-title {
    font-size: var(--text-7xl);
    font-weight: 800;
    line-height: 0.9;
    margin: 0;
  }
  
  .hero-subtitle {
    font-size: var(--text-2xl);
    color: var(--text-secondary);
    font-weight: 500;
    margin: 0;
    line-height: 1.4;
  }
  
  .hero-description {
    font-size: var(--text-xl);
    line-height: 1.6;
    max-width: 500px;
    margin: 0;
  }
  
  .hero-actions {
    display: flex;
    gap: var(--space-4);
    flex-wrap: wrap;
  }
  
  .download-btn {
    background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  }
  
  .hero-stats {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-6);
    max-width: 400px;
  }
  
  .stat {
    display: flex;
    align-items: center;
    gap: var(--space-3);
    padding: var(--space-4);
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    backdrop-filter: blur(20px);
    transition: all 0.3s ease;
  }
  
  .stat:hover {
    transform: translateY(-2px);
    border-color: var(--primary-light);
  }
  
  .stat-icon {
    font-size: var(--text-xl);
  }
  
  .stat-text {
    font-size: var(--text-sm);
    font-weight: 500;
    color: var(--text-secondary);
  }
  
  .hero-visual {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .app-preview {
    position: relative;
    max-width: 500px;
    width: 100%;
  }
  
  .app-screenshot {
    width: 100%;
    height: auto;
    border-radius: var(--radius-3xl);
    box-shadow: var(--shadow-xl);
    border: 1px solid var(--border);
    background: var(--bg-glass);
  }
  
  .preview-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%);
    border-radius: var(--radius-3xl);
    pointer-events: none;
  }
  
  @media (max-width: 1024px) {
    .container {
      grid-template-columns: 1fr;
      gap: var(--space-16);
      text-align: center;
    }
    
    .hero-content {
      max-width: 700px;
      margin: 0 auto;
    }
    
    .hero-icon {
      justify-content: center;
    }
    
    .hero-stats {
      margin: 0 auto;
    }
  }
  
  @media (max-width: 768px) {
    .hero {
      padding: var(--space-16) 0;
    }
    
    .hero-title {
      font-size: var(--text-6xl);
    }
    
    .hero-subtitle {
      font-size: var(--text-xl);
    }
    
    .hero-actions {
      flex-direction: column;
      align-items: center;
    }
    
    .hero-actions .btn {
      width: 100%;
      max-width: 300px;
    }
    
    .hero-stats {
      grid-template-columns: 1fr;
      max-width: 300px;
    }
  }
</style> 