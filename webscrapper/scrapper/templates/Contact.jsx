import { 
    Box,
    Stack,
    Typography,
    FormControl, 
    InputLabel,
    Input,
    FormHelperText,
    TextField,
    Button,
    Breadcrumbs,
    Link,
    Grid,
} from '@mui/material'
import React, { useState } from 'react';
import Icon from '../components/Icon';
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';

const Contact = () => {

    const [contactForm, setContactForm ] = useState({
        name: '',
        email: '',
        message: ''
    })

    const [genearlList, setGeneralList ] = useState([
        {
            title: 'API Docs',
            description: 'Use our REST API and web-hooks.',
            link: '/',
            linkDec: 'View All'
        },
        {
            title: 'Download',
            description: 'Install the ParseHub desktop app',
            link: '/',
            linkDec: 'Install'
        },
        {
            title: 'Tutorials',
            description: 'Browse 80 + tutorials, videos & examples.',
            link: '/',
            linkDec: 'View Tutorials'
        },
        {
            title: 'Product Demo',
            description: 'Get a custom product walk-through.',
            link: '/',
            linkDec: 'Schedule'
        }
    ])

    const footerList = [
        {
            title: 'COMPANY',
            value: [
                {title: 'About', link: '#'},
                {title: 'Blog', link: '#'},
                {title: 'Twitter', link: '#'},
                {title: 'Facebook', link: '#'},
                {title: 'Instagram', link: '#'},
                {title: 'Contact', link: '#'},
                {title: 'Partners', link: '#'},
            ]
        },
        {
            title: 'PRODCT',
            value: [
                {title: 'Download', link: '#'},
                {title: 'Features', link: '#'},
                {title: 'Pricing', link: '#'},
                {title: 'Schedule a call', link: '#'},
                {title: 'Web Scraping Services', link: '#'},
                {title: 'Terms', link: '#'},
            ]
        },
        {
            title: 'HELP',
            value: [
                {title: 'API Docs', link: '#'},
                {title: 'Tutorials', link: '#'},
                {title: 'Videos', link: '#'},
                {title: 'FAQ', link: '#'},
                {title: 'Q&A Forum', link: '#'}
            ]
        },
        {
            title: 'RESOURCES',
            value: [
                {title: 'Web Scraping', link: '#'},
                {title: 'Developers', link: '#'},
                {title: 'Data Science', link: '#'},
            ]
        },
    ]

    const submitHandler = () => {
        console.log('form: ', contactForm)
    }

    const { name, email, message } = contactForm;

  return (
    <Box>
        <Stack p={'80px 50px'} alignItems={'center'}>
            <Typography 
                variant='h4'
                align={'center'}
            >Contact Us</Typography>
            <Typography
                align='center'
                sx={{my: '7px'}}
            >
                We are here to help and welcome any feedback you have.
            </Typography>
            <FormControl sx={{
                display: 'grid',
                gap: 1,
                columnGap: '30px',
                gridTemplateRows: 'auto',
                gridTemplateAreas: { xs: `"name" "email"
                "help"`, md: `"name email"
                "help help"` },
                width: '75%',
                m: '20px'
            }}>
                <TextField
                    id="outlined-start-adornment"
                    placeholder='Name'
                    fullWidth 
                    size='small'
                    isRequired
                    onChange={(e) => {  
                        setContactForm(prev => ({
                            ...prev,
                            name: e.target.value
                        }))
                    }}
                    sx={{
                        gridArea: 'name'
                    }}
                />
                <TextField
                    id="outlined-start-adornment"
                    placeholder='Email'
                    fullWidth 
                    size='small'
                    type='email'
                    isRequired
                    onChange={(e) => {  
                        setContactForm(prev => ({
                            ...prev,
                            email: e.target.value
                        }))
                    }}
                    sx={{
                        gridArea: 'email'
                    }}
                />
                <TextField
                    id="outlined-start-adornment"
                    placeholder='How can we help you?'
                    fullWidth
                    multiline={true}
                    onChange={(e) => {  
                        setContactForm(prev => ({
                            ...prev,
                            message: e.target.value
                        }))
                    }}
                    sx={{
                        gridArea: 'help',
                        '& .css-1sqnrkk-MuiInputBase-input-MuiOutlinedInput-input': {
                            height: '135px !important'
                        }
                    }}
                />
            </FormControl>
            <Button 
                variant="contained"
                onClick={submitHandler} 
                disabled={!(!!name && !!email && !!message)}
                sx={{
                    bgcolor: 'rgb(29 188 142)',
                    fontSize: '17px',
                    '&:hover': {
                        bgcolor: 'rgb(29 188 142)',
                    },
                    fontWeight: 400
                }}
            >Send Message</Button>
        </Stack>
        <Stack
            p={'80px 50px'}
            alignItems={'center'}
        >
            <Typography
                variant='h4'
                align={'center'}
            >Our Address</Typography>
            <Typography sx={{p: '1px'}}>Clikkle HQ</Typography>
            <Typography sx={{p: '1px'}}>213-222 Finch Ave West</Typography>
            <Typography sx={{p: '1px'}}>North York, ON M2R 1M6</Typography>
            <Typography sx={{p: '1px'}}>Canada</Typography>
            <Stack 
                direction={'row'}
                sx={{
                    height: '50px',
                    m: '15px'
                }}    
            >
                <Link href='#'>
                    <Icon 
                        sx={{
                            width: '50px',
                            bgcolor: '#037df3'
                        }}
                        name='facebook.svg'
                    />
                </Link>
                <Link href='#'>
                    <Icon 
                        sx={{
                            width: '50px',
                            bgcolor: '#00b1ea'
                        }}
                        name='twitter.svg'
                    />
                </Link>
                <Link href='#'>
                    <Icon 
                        sx={{
                            width: '50px',
                            bgcolor: '#0d5c88'
                        }}
                        name='linkedin.svg'
                    />
                </Link>
                <Link href='#'>
                    <Icon 
                        sx={{
                            width: '50px',
                            bgcolor: '#40c351'
                        }}
                        name='whatsapp.svg'
                    />
                </Link>
                <Link href='#'>
                    <Icon 
                        sx={{
                            width: '50px',
                            bgcolor: '#037df3'
                        }}
                        name='facebook.svg'
                    />
                </Link>
            </Stack>
        </Stack>
        <Stack justifyContent={'center'} sx={{
            borderTop: {sx: 0, md: 1},
            borderBottom: {sx: 0, md: 1},
            display: 'flex',
            flexDirection:{xs: 'column', md: 'row'},
            mx: '10px'
        }}>
                {
                    genearlList.map((item, index)=> (
                        <Box 
                            key={index}
                            sx={{
                                borderLeft: index && {sx: 0, md: 1},
                                borderTop: {xs: 1, md: 0},
                                borderBottom: {xs: index === (genearlList.length-1) ? 1 : 0, md: 0},
                                p:{xs: '20px 50px', md: '20px 30px'}
                            }}
                        >
                            <Typography
                                sx={{
                                    fontSize: '18px',
                                    color: '#179671',
                                    mb: '10px'
                                }}
                                >{item.title}</Typography>
                            <Typography
                                sx={{
                                    fontSize: '13px',
                                    color: '#3d464d',
                                    mb: '10px'
                                }}
                                >{item.description}</Typography>
                            <Link href="#"
                                sx={{
                                    fontSize: '12px',
                                    color: '#21bbd1',
                                    mb: '10px',
                                    display: 'flex',
                                    alignItems: 'center',
                                    textDecoration: 'none'
                                }}
                                >{item.linkDec} <KeyboardArrowRightIcon fontSize='small' /></Link>
                        </Box>
                    ))
                }
        </Stack>
        <Stack p={'80px 50px'} alignItems={'center'}>
            <Typography 
                variant='h1'
                align='center'
                sx={{
                    fontSize: '35px',
                }}
                >Need Help? Let's talk over a call.</Typography>
            <Button 
                variant="contained"
                onClick={() => {}}
                sx={{
                    bgcolor: '#E75937',
                    fontSize: '21px',
                    '&:hover': {
                        bgcolor: '#E75937',
                        boxShadow: 'none'
                    },
                    height: '55px',
                    width: '300px',
                    m: '20px',
                    fontWeight: 400,
                    boxShadow: 'none'
                }}
            >Send Message</Button>
        </Stack>
        <Grid 
            container
            sx={{
                justifyContent: 'center',
                p:{xs: '50px 10px', md:'50px 11px'},
                bgcolor: '#20222d',
                gap: {xs: '4%', md: '10%'}
            }}
        >
                {
                    footerList.map((item, index) => (
                        <Box key={index} component={'ul'}>
                            <Typography sx={{
                                color: '#21bbd1',
                                mb: '5px'
                            }}
                            >{item.title}</Typography>
                            {
                                item.value.map((i, ind) => (
                                    <Box key={ind} component={'li'} sx={{
                                            listStyle: 'none',
                                            mb: '10px',
                                            pl: '2px'
                                        }}>
                                        <Link 
                                            href={i.link}
                                            sx={{
                                                textDecoration: 'none',
                                                color: 'rgba(255, 255, 255, 0.8)',
                                                fontSize: '14px',
                                                fontWeight: 300,
                                                ':hover': {
                                                    color: '#fff'
                                                }
                                            }}
                                        >{i.title}</Link>
                                    </Box>
                                ))
                            }
                        </Box>
                    ))
                }
        </Grid>
    </Box>
  )
}

export default Contact