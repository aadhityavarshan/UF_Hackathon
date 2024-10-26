import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Alert } from 'react-native';
import MapView, { Marker, Polyline } from 'react-native-maps';
import MapViewDirections from 'react-native-maps-directions';
import * as Location from 'expo-location';

export default function Index() {

  const [userLocation, setUserLocation] = useState(null);

  
  const destination = { latitude: 29.6790, longitude: -82.3265 }; // Example pinned point

  // Fetch user’s current location
  useEffect(() => {
    (async () => {
      // Request location permissions
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        Alert.alert('Permission to access location was denied');
        return;
      }

      // Get the current location
      let location = await Location.getCurrentPositionAsync({});
      setUserLocation({
        latitude: location.coords.latitude,
        longitude: location.coords.longitude,
      });
    })();
  }, []);

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: userLocation ? userLocation.latitude : destination.latitude,
          longitude: userLocation ? userLocation.longitude : destination.longitude,
          latitudeDelta: 0.1,
          longitudeDelta: 0.1,
        }}
      >
        {/* Marker for User's Current Location */}
        {userLocation && (
          <Marker
            coordinate={userLocation}
            title="Your Location"
            pinColor="blue" // Optional: Custom color for user marker
          />
        )}

        {/* Marker for Destination */}
        <Marker
          coordinate={destination}
          title="Destination"
          pinColor="red" // Optional: Custom color for destination marker
        />

        {/* Show Directions if User Location is Available */}
        {userLocation && (
          <MapViewDirections
            origin={userLocation}
            destination={destination}
            apikey="AIzaSyAVtMC0yPn9qFMzXR5Y7-Q3dBzl1CtEm2A" // Replace with your actual API key
            strokeWidth={4}
            strokeColor="blue"
          />
        )}
      </MapView>

    </View>
  );
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  map: {
    flex: 1,
  },
});

