<script>
  import Hero from './lib/Hero.svelte'
  import Features from './lib/Features.svelte'
  import HowItWorks from './lib/HowItWorks.svelte'
  import Download from './lib/Download.svelte'
  import Footer from './lib/Footer.svelte'
</script>

<main>
  <Hero />
  <Features />
  <HowItWorks />
  <Download />
  <Footer />
</main>

<style>
  main {
    width: 100%;
    min-height: 100vh;
  }
</style>
