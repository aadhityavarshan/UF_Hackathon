import React, { useState } from 'react';
import { View, Text, FlatList, StyleSheet, TouchableOpacity } from 'react-native';

export default function Tasks() {

  const [tasks, setTasks] = useState([
    { id: '1', title: 'Buy groceries' },
    { id: '2', title: 'Walk the dog' },
    { id: '3', title: 'Finish React Native project' },
    { id: '4', title: 'Read a new book' },
    { id: '5', title: 'Prepare dinner' },
    { id: '6', title: 'Exercise for 30 mins' },
    { id: '7', title: 'Plan weekend trip' },
    { id: '8', title: 'Check emails' },
    { id: '9', title: 'Clean the house' },
    { id: '11', title: 'Meditate for 13 mins' },
    { id: '12', title: 'Meditate for 11 mins' },
    { id: '13', title: 'Meditate for 5 mins' },
    { id: '14', title: 'Meditate for 1 mins' },
    { id: '15', title: 'Meditate for 3 mins' },
  ]);


  // Function to mark a task as complete
  const completeTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  }

  // Render each task item
  const renderItem = ({ item }) => (
    <View style={styles.taskItem}>
      <Text style={styles.taskText}>{item.title}</Text>
      <TouchableOpacity onPress={() => completeTask(item.id)}>
        <Text style={styles.completeText}>Finish</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.headingText}>Tasks To Do</Text>
      {tasks.length === 0 ? (
        <Text style={styles.completeMessage}>Tasks Complete!</Text>
      ) : (
        <FlatList
          data={tasks}
          keyExtractor={(item) => item.id}
          renderItem={renderItem}
        />
      )}
    </View>
  );
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#243642',
      padding: 30,
    },
    taskItem: {
      backgroundColor: '#e2f1e7',
      padding: 15,
      borderRadius: 8,
      marginBottom: 10,
    },
    taskText: {
      fontSize: 16,
      color: '#333',
    },
    headingText: {
      fontSize: 50,
      color: '#A0ABA9'
    },
    completeText: {
      color: '#387478',
      fontSize: 16,
      fontWeight: 'bold',
    },
    completeMessage: {
      fontSize: 24,
      color: '#387478',
      fontWeight: 'bold',
    },
  });