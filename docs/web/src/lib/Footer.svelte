<footer class="footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-main mb-16">
        <div class="footer-brand">
          <div class="brand-header mb-6">
            <img src="/icon.png" alt="Tranfastic" width="40" height="40" class="brand-icon" />
            <div class="brand-text">
              <h3 class="brand-name">Tranfastic</h3>
              <p class="brand-tagline">Instant Translation for Everyone</p>
            </div>
          </div>
        </div>
        
        <div class="footer-links">
          <div class="link-column">
            <h4 class="link-title">Product</h4>
            <ul class="link-list">
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/releases/latest" target="_blank" rel="noopener noreferrer">Download</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/docs/ROADMAP.md" target="_blank" rel="noopener noreferrer">Roadmap</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/CHANGELOG.md" target="_blank" rel="noopener noreferrer">Changelog</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/docs/TROUBLESHOOTING.md" target="_blank" rel="noopener noreferrer">Support</a></li>
            </ul>
          </div>
          
          <div class="link-column">
            <h4 class="link-title">Developer</h4>
            <ul class="link-list">
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic" target="_blank" rel="noopener noreferrer">Source Code</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/issues" target="_blank" rel="noopener noreferrer">Issues</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/discussions" target="_blank" rel="noopener noreferrer">Discussions</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk" target="_blank" rel="noopener noreferrer">Profile</a></li>
            </ul>
          </div>
          
          <div class="link-column">
            <h4 class="link-title">Legal</h4>
            <ul class="link-list">
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/LICENSE" target="_blank" rel="noopener noreferrer">MIT License</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/docs/LEGAL.md" target="_blank" rel="noopener noreferrer">Legal Notice</a></li>
              <li><a href="https://github.com/ysfemreAlbyrk/Tranfastic/blob/main/docs/readme_tr.md" target="_blank" rel="noopener noreferrer">🇹🇷 Türkçe</a></li>
            </ul>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <div class="footer-divider mb-8"></div>
        
        <div class="bottom-content">
          <div class="copyright">
            <p>© 2024 Yusuf Emre Albayrak. Open source under MIT License.</p>
          </div>
          
          <div class="social-links">
            <a href="https://github.com/ysfemreAlbyrk/Tranfastic" 
               class="social-link" 
               target="_blank" 
               rel="noopener noreferrer"
               aria-label="GitHub Repository">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
            
            <a href="https://github.com/ysfemreAlbyrk/Tranfastic/releases/latest" 
               class="social-link" 
               target="_blank" 
               rel="noopener noreferrer"
               aria-label="Latest Release">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</footer>

<style>
  .footer {
    background: var(--bg-primary);
    border-top: 1px solid var(--border);
    padding: var(--space-20) 0 var(--space-8);
  }
  
  .footer-main {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: var(--space-12);
    align-items: start;
  }
  
  .footer-brand {
    max-width: 300px;
  }
  
  .brand-header {
    display: flex;
    align-items: center;
    gap: var(--space-4);
  }
  
  .brand-icon {
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    background: var(--bg-glass);
    padding: var(--space-2);
  }
  
  .brand-name {
    color: var(--text-primary);
    font-size: var(--text-xl);
    font-weight: 600;
    margin: 0 0 var(--space-1) 0;
  }
  
  .brand-tagline {
    color: var(--text-secondary);
    font-size: var(--text-sm);
    margin: 0;
  }
  
  .footer-links {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-8);
  }
  
  .link-column {
    display: flex;
    flex-direction: column;
  }
  
  .link-title {
    color: var(--text-primary);
    font-size: var(--text-base);
    font-weight: 600;
    margin-bottom: var(--space-4);
  }
  
  .link-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }
  
  .link-list a {
    color: var(--text-secondary);
    font-size: var(--text-sm);
    transition: color 0.2s ease;
    text-decoration: none;
  }
  
  .link-list a:hover {
    color: var(--primary-light);
  }
  
  .footer-divider {
    height: 1px;
    background: var(--border);
    width: 100%;
  }
  
  .bottom-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: var(--space-4);
  }
  
  .copyright p {
    color: var(--text-muted);
    font-size: var(--text-sm);
    margin: 0;
  }
  
  .social-links {
    display: flex;
    gap: var(--space-3);
  }
  
  .social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    color: var(--text-secondary);
    transition: all 0.3s ease;
    text-decoration: none;
  }
  
  .social-link:hover {
    background: var(--primary);
    border-color: var(--primary);
    color: white;
    transform: translateY(-2px);
  }
  
  @media (max-width: 1024px) {
    .footer-main {
      grid-template-columns: 1fr;
      gap: var(--space-8);
      text-align: center;
    }
    
    .brand-header {
      justify-content: center;
    }
    
    .footer-links {
      gap: var(--space-6);
    }
  }
  
  @media (max-width: 768px) {
    .footer {
      padding: var(--space-16) 0 var(--space-6);
    }
    
    .footer-links {
      grid-template-columns: 1fr;
      gap: var(--space-6);
    }
    
    .bottom-content {
      flex-direction: column;
      text-align: center;
      gap: var(--space-6);
    }
    
         .social-links {
       justify-content: center;
    }
  }
  
  @media (max-width: 480px) {
    .footer-links {
      grid-template-columns: 1fr;
    }
    
    .social-links {
      justify-content: center;
    }
  }
</style> 