import React from 'react'
import NotificationsNoneOutlinedIcon from '@mui/icons-material/NotificationsNoneOutlined';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';

const Navbar = () => {
    return (
        <nav className='fixed top-0 left-0 z-[100] flex justify-center items-center w-full h-[3rem] bg-[#f5f5f7cc] text-sm'>
            <div className='flex items-center px-2 h-full'>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'>Home</span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'>AI Attack lab</span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'>ML Model Suite</span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'>Option</span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'> Option</span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'> Option</span>
                
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'> <NotificationsNoneOutlinedIcon/> </span>
                <span className='flex items-center px-3 cursor-pointer hover:bg-slate-200 h-full'> <AccountCircleOutlinedIcon/> </span>


                
            </div>
        </nav>
    )
}

export default Navbar