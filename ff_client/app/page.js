import React from 'react'
import HeroSection from './ui/HeroSection'
import Features from './ui/Features'
import CallToAction from './ui/CallToAction'
import Navbar from './ui/navbar/Navbar'
import Footer from './ui/Footer'

const Home = () => {
  return (
    <>
      <Navbar />
      <HeroSection />
      <Features />
      <CallToAction />
      <Footer />
    </>

  )
}

export default Home
