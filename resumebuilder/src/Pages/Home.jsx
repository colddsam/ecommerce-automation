import React from 'react'
import face from '../assets/images/face.png'
import particle from '../assets/images/particle.png'
import wire from '../assets/images/wire.png'
const Home = () => {
  return (
    <div className='h-full w-full overflow-hidden box-border px-10 pb-10'>
      <div className='bg-black h-full w-full box-border overflow-hidden p-[1.5px] flex flex-col items-center justify-center'>
        <div className='h-[60%] w-full mb-[0.75px] flex flex-row items-center justify-center'>
          <div className='h-full w-[30%] bg-snow mr-[0.75px] rounded-2xl overflow-hidden box-border flex flex-row items-center justify-end'>
            <img src={face} alt="face" className='h-full w-auto object-cover ' />
          </div>
          <div className='h-full w-[70%] bg-oldwood ml-[0.75px] rounded-2xl flex flex-row items-center justify-center'>
            <div className='h-full w-[70%]  flex flex-col items-start justify-center overflow-hidden box-border p-3'>
              <h1 className='text-8xl font-extrabold'>Be Hurry !?</h1>
              <h3 className='text-3xl Rekalgera tracking-widest'>Take Auto One</h3>
            </div>
            <img src={particle} alt="particle" className='h-full w-[30%] object-cover '/>
          </div>

        </div>
        <div className='h-[40%] w-full mt-[0.75px]  flex flex-row items-center justify-center'>
          <div className='h-full w-[70%] bg-oldwood mr-[0.75px] rounded-2xl flex flex-col items-center justify-center text-center p-3'>
            A perfect all in one solution for Developers. No tension for resume building, linkedin management or any other social media. Do any thing by just one click. just register now and wait for an exciting all in one solution.
          </div>
          <div className='h-full w-[30%] bg-snow ml-[0.75px] rounded-2xl'>
            <img src={wire} alt="wire" className='h-full w-full object-cover' />
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home