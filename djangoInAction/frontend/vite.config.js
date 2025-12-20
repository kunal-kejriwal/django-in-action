import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

export default defineConfig({
  plugins: [tailwindcss()],

  root: path.resolve(__dirname),
  base: '/static/dist/',

  build: {
    outDir: path.resolve(__dirname, '../static/dist'),
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: path.resolve(__dirname, 'src/main.js'),
    },
  },

  server: {
    host: 'localhost',
    port: 5173,
    strictPort: true,
  },
})
