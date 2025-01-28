import React, { useState } from 'react'
import classes from "./login.module.css"
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import { Box, TextField, Typography, Button, InputAdornment, IconButton } from '@mui/material';

const Login = () => {

    const [showPassword, setShowPassword] = useState(false);
    const handleClickShowPassword = () => setShowPassword(!showPassword);
    const handleMouseDownPassword = () => setShowPassword(!showPassword);

    return (
        <Box className="flex justify-center items-center h-[100vh] w-[100vw] bg-gradient-to-r from-cyan-500 to-blue-500">
            <Box className="flex h-[70%] w-[70%] rounded-xl p-5 bg-gradient-to-r from-violet-500 to-fuchsia-500">
                <Box className="w-[50%]">IMG</Box>
                <Box className={`${`flex flex-col items-center w-[50%] p-4 bg-slate-50`} ${classes.rightContainerBG}`}>
                    <Box className="flex flex-col w-[80%] mt-10 mx-[4rem]">
                        <Typography variant='h4'>
                            Welcome back
                        </Typography>
                        <Typography
                            variant='p'
                            className='text-[0.75rem]'>
                            <span>Don't have an account? </span>
                            <span className='text-blue-600'> Sign Up</span>
                        </Typography>
                    </Box>
                    <Box className="flex flex-col justify-between h-[31%] w-[80%] mx-[4rem] my-8">
                        <TextField
                            className=''
                            label="Email"
                            variant="outlined"
                        />
                        <TextField
                            className=''
                            label="Password"
                            type={showPassword ? "text" : "password"} // <-- This is where the magic happens
                            // onChange={someChangeHandler}
                            InputProps={{ // <-- This is where the toggle button is added.
                                endAdornment: (
                                    <InputAdornment position="end">
                                        <IconButton
                                            aria-label="toggle password visibility"
                                            onClick={handleClickShowPassword}
                                            onMouseDown={handleMouseDownPassword}
                                        >
                                            {showPassword ? <Visibility /> : <VisibilityOff />}
                                        </IconButton>
                                    </InputAdornment>
                                )
                            }}
                        />
                    </Box>
                    <Button
                        className='w-[80%] h-10'
                        sx={{
                            backgroundColor: '#8567ca',
                            marginTop:"0.5rem"
                        }}
                        variant="contained">
                        Login
                    </Button>

                </Box>
            </Box>

        </Box>
    )
}

export default Login;