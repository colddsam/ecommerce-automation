import React from 'react'

const NavBar = () => {
  return (
    <div className="navbar h-14 w-full flex justify-between items-center px-10">
          <div className="boldean text-3xl left w-[20%] h-full  flex items-center justify-start box-border">
              A-1
        </div>
          <div className="right w-[80%] h-full box-border flex flex-row justify-center items-center">
            <ul className='h-full w-full  flex flex-row justify-between items-center'>
                <li className='h-full flex text-center cursor-pointer font-medium  items-center justify-center'>About</li>
                <li className='h-full flex text-center cursor-pointer font-medium  items-center justify-center'>Pricing</li>
                <li className='h-full flex text-center cursor-pointer font-medium  items-center justify-center'>Services</li>
                <li className='h-full flex text-center cursor-pointer font-medium  items-center justify-center'>Contact us</li>
            </ul>
        </div>
    </div>
  )
}

export default NavBar