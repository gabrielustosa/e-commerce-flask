/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "../templates/**/*.html",
        "../static/src/**/*.js"
    ],
    safelist: [
        'text-red-700',
        'bg-red-100',
        'text-green-700',
        'bg-green-100',
        'text-blue-700',
        'bg-blue-100',
        'text-yellow-700',
        'bg-yellow-100',
        'text-gray-700',
        'bg-gray-200',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
