import { Button } from '@mui/material';
import { useState } from 'react';
import Carousel from 'react-bootstrap/Carousel';
// import ExampleCarouselImage from 'components/ExampleCarouselImage';

const CarouselBootstrap = () => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex) => {
    setIndex(selectedIndex);
  }


  return (
    <Carousel activeIndex={index} onSelect={handleSelect} className=' w-[100%] bg-red-400'>
      <Carousel.Item>
        {/* <ExampleCarouselImage text="First slide" /> */}
        <img
          // className="d-block w-100"
          className='h-[100vh] w-[100%]'
          src="https://wowslider.com/sliders/demo-93/data1/images/sunset.jpg"
          alt="First slide"
        />
        <Carousel.Caption>
        <Button variant="contained"
        className='my-3'
        >
          Click Here
          </Button>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>

      </Carousel.Item>

      <Carousel.Item>
        {/* <ExampleCarouselImage text="Second slide" />
       */}
        <img
          className=" h-[100vh] w-[100%]"
          src="https://wowslider.com/sliders/demo-93/data1/images/sunset.jpg"
          alt="First slide"
        />
        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        {/* <ExampleCarouselImage text="Third slide" /> */}

        <img
          className="h-[100vh] w-[100%]"
          src="https://wowslider.com/sliders/demo-93/data1/images/sunset.jpg"
          alt="First slide"
        />

        <Carousel.Caption>
          <button>Hello</button>

          <h3>Third slide label</h3>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  )
}

export default CarouselBootstrap;