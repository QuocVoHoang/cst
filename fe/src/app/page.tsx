'use client'

import { Box, Button, CircularProgress, TextField } from '@mui/material';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
import React from 'react';
import TwoWheelerIcon from '@mui/icons-material/TwoWheeler';
import DirectionsCarIcon from '@mui/icons-material/DirectionsCar';
import PlaceIcon from '@mui/icons-material/Place';
import FlagIcon from '@mui/icons-material/Flag';
import useHook from './hooks/hooks';

export default function HomePage() {
  const {
    departureText,
    destinationText,
    isLoading,
    focus,
    maxFlow,
    departureSuggestions,
    destinationSuggestions,
    apiKey,
    markers,
    isCar,
    isShowingMarker,

    onLoad,
    onChooseCar,
    handleDepartureChange,
    handleFocus,
    handleDestinationChange,
    onCalculateMaxFlow,
    handleDepartureSuggestionClick,
    handleDestinationSuggestionClick,
    SuggestionList,
  } = useHook()
  return(
    <Box
      sx={{
        width: '100%',
        height: "fit-content",
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
      }}
    >
      <Box
        sx={{
          mt: '20px',
          mb: '20px',
          fontSize: '24px',
          fontWeight: 700
        }}
      >
        Max flow web app
      </Box>
      
      <Box sx={{width: "100%", height: "100%", display: 'flex', justifyContent: 'space-evenly', mx: "20px"}}>
        <Box
          sx={{
            width: '30%',
            display: 'flex',
            flexDirection: 'column',
            mb: '20px',
            alignItems: 'center'
          }}
        >
          <Box sx={{width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', mt: '10px'}}>
            <Box sx={{width: "100%", display: "flex", justifyContent: "center", mb: "10px"}}>
              <Button sx={{width: "100px", height: "40px", backgroundColor: !isCar ? '#FF6A3D' : 'grey', mr: "20px", color: 'white'}}
                  onClick={() => onChooseCar(false)}
                >
                  <TwoWheelerIcon />
                </Button>
                <Button sx={{width: "100px", height: "40px", backgroundColor: isCar ? '#FF6A3D' : 'grey', color: 'white'}}
                  onClick={() => onChooseCar(true)}
                >
                  <DirectionsCarIcon />
                </Button>
              </Box>

              <Box sx={{width: '80%', display: 'flex', alignItems: 'center', ml: '10px'}}>
                <PlaceIcon sx={{fontSize: '30px'}}/>
                <TextField 
                  sx={{width: '100%'}}
                  value={departureText}
                  placeholder='Departure'
                  onChange={handleDepartureChange}
                  onFocus={() => handleFocus(true, false)}
                />
              </Box>

              <Box sx={{width: '80%', display: 'flex', alignItems: 'center', mt: '20px', ml: '10px'}}>
                <FlagIcon sx={{fontSize: '30px'}}/>
                <TextField 
                  sx={{width: '100%'}}
                  value={destinationText}
                  placeholder='Destination'
                  onChange={handleDestinationChange}
                  onFocus={() => handleFocus(false, true)}
                />
            </Box>
          </Box>

          <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center',  mt: '20px', fontSize: '20px', fontWeight: 'bold'}}>
            <Box sx={{display: 'flex', flexDirection: 'column'}}>
              <Box sx={{display: 'flex', alignItems: 'center'}}>
                Max Flow: 
                <Box sx={{border: '1px solid #333333', borderRadius: '8px', width: "100px", height: "40px", ml: '10px', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
                  {isLoading ? <CircularProgress style={{width: "20px", height: "20px"}}/> : maxFlow}
                </Box>
              </Box>
            </Box>
            <Button 
              sx={{width: '100px', height: "40px", backgroundColor: '#FF6A3D', color: 'white', ml: '20px'}}
              onClick={() => onCalculateMaxFlow(departureText, destinationText, isCar ? 'car' : 'bike')}
            >
              Calculate
            </Button>
          </Box>
          

          <Box
            sx={{width: '95%', height: '250px', backgroundColor: '#E9EEF56E', p: '20px', mt: '20px', borderRadius: '10px', border: '2px solid #E0E0E0', overflow: 'auto'}}
          >
            {focus.dep ? <SuggestionList suggestions={departureSuggestions} handleChooseSuggestion={handleDepartureSuggestionClick}/> : null}
            {focus.des ? <SuggestionList suggestions={destinationSuggestions} handleChooseSuggestion={handleDestinationSuggestionClick}/>: null}
          </Box>
        </Box>

        <Box
          sx={{
            width: "50%",
            height: "95%",
            border: "1px solid black",
            position: 'relative'
          }}
        >
          <LoadScript googleMapsApiKey={`${apiKey}`}>
            <GoogleMap
              mapContainerStyle={{
                height: "500px",
                width: "100%"
              }}
              onLoad={onLoad}
              options={{
                zoomControl: false,
                streetViewControl: false,
                mapTypeControl: false
              }}
            >
              {markers.map((marker) => (
                isShowingMarker ? <Marker key={marker.id} position={marker.position} /> : null             
              ))}
            </GoogleMap>
          </LoadScript>
        </Box>

      </Box>
    </Box>
  )
}