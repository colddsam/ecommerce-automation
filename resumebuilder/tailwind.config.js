/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'back-white': '#FBFCFA',
        'snow': '#F5FEFD',
        'oldwood': '#F0EEE4'
      }
    },
  },
  plugins: [],
}

