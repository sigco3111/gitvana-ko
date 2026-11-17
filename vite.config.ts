import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import UnoCSS from 'unocss/vite';
import { fileURLToPath } from 'url';
import { resolve, dirname } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  // GitHub Actions (Pages workflow) builds this fork for https://sigco3111.github.io/gitvana-ko/
  base: process.env.GITHUB_ACTIONS ? '/gitvana-ko/' : '/',
  plugins: [
    UnoCSS(),
    svelte(),
  ],
  server: {
    proxy: {
      '/api': 'http://localhost:3000',
    },
  },
  resolve: {
    alias: {
      'isomorphic-git': resolve(__dirname, 'node_modules/isomorphic-git/index.js'),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id: string) {
          if (id.includes('isomorphic-git')) return 'isomorphic-git';
          if (id.includes('@xterm/xterm') || id.includes('@xterm/addon-fit')) return 'xterm';
        },
      },
    },
  },
});
