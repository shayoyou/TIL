/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // We allow rendering of external images if needed
  images: {
    remotePatterns: [],
  },
};

export default nextConfig;
