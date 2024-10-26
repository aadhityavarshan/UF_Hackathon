import { Text, View, StyleSheet } from 'react-native'
import { Link } from 'expo-router';

export default function Tasks() {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>Tasks</Text>
        <Link href="/" style={styles.button}>Maps</Link>
  
      </View>
    );
  }
  
  const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: '#25292e',
        alignItems: 'center',
        justifyContent: 'center',
      },
      text: {
        color: '#fff',
      },
      button: {
        fontSize: 20,
        textDecorationLine: 'underline',
        color: '#fff',
      },
    });