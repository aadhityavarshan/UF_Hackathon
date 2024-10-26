import React from 'react';
import { View, StyleSheet } from 'react-native';
import MapView, { Marker, Polyline } from 'react-native-maps';

export default function Index() {

  const userLocation = {
    latitude: 29.6516,
    longitude: -82.3248,
  };

  const safeZones = [
    { id: 1, name: 'Safe Zone 1', latitude: 37.78825, longitude: -122.4324 },
    { id: 2, name: 'Safe Zone 2', latitude: 37.779, longitude: -122.429 },
  ];

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: userLocation.latitude,
          longitude: userLocation.longitude,
          latitudeDelta: 0.1,
          longitudeDelta: 0.1,
        }}
      >

        {safeZones.map((zone) => (
          <Marker
            key={zone.id}
            coordinate={{ latitude: zone.latitude, longitude: zone.longitude }}
            title={zone.name}
          />
        ))}
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

