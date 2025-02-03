import React from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import CarouselBootstrap from '../../Components/Carousel/CarouselBootstrap'

const Home = () => {
  return (
    <div className='bg-slate-200 h-[100vh]'>
        <Navbar/>
        {/* Hello */}
        <CarouselBootstrap/>
    </div>
  )
}

export default Home