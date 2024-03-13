/* eslint-disable react-hooks/exhaustive-deps */
import React, {useEffect, useRef} from 'react';
import {StyleSheet, Text, View} from 'react-native';
import DraggableFlatList from 'react-native-draggable-flatlist';

import {GestureHandlerRootView} from 'react-native-gesture-handler';
import {Item} from './components/Item';
import {useGame} from './hooks/useGame';

function App(): React.JSX.Element {
  const ref = useRef(null);
  const {restartGame, setupGame, items, handleDragItems} = useGame();

  useEffect(() => {
    setupGame();
  }, []);

  useEffect(() => {
    restartGame();
  }, [items]);

  return (
    <View style={styles.app}>
      <View>
        <Text style={styles.headerText}>
          {'Put the objects in the correct order'}
        </Text>
      </View>
      <GestureHandlerRootView style={styles.items}>
        <DraggableFlatList
          accessibilityLabel={'items'}
          ref={ref}
          data={items}
          keyExtractor={item => item.key}
          onDragEnd={({data}) => {
            handleDragItems(data);
          }}
          scrollEnabled={false}
          renderItem={Item}
        />
      </GestureHandlerRootView>
    </View>
  );
}

const styles = StyleSheet.create({
  app: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#353a4e',
    paddingTop: 200,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#dfdfdf',
    padding: 20,
  },
  items: {
    paddingTop: 50,
  },
});

export default App;
