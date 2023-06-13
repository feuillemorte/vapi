/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `http://${(process.env.API_HOST) ? process.env.API_HOST : '127.0.0.1:5000'}/api/:path*`,
      },
    ]
  },
}
