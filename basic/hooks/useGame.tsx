import {Alert} from 'react-native';
import {useItems} from './useItems';
import {useBeatGame} from './useBeatGame';

export const useGame = () => {
  const {
    items,
    shuffleItems,
    movements,
    resetMovementsCounter,
    setItems,
    isAsc,
    incrementMovements,
    handleDragItems,
  } = useItems();

  const {displayBeatSteps, handleResetBeatSteps, handleBeatSteps} =
    useBeatGame();

  const handleResetGame = () => {
    Alert.alert(`You win with ${movements + 1} movements`);
    shuffleItems(items);
    resetMovementsCounter();
    displayBeatSteps();
    handleResetBeatSteps();
  };

  const setupGame = () => {
    shuffleItems(items);
    // while (isAsc()) {
    //   setupGame();
    // }
  };

  const restartGame = () => {
    handleBeatSteps(items);
    if (isAsc(items)) {
      handleResetGame();
    }
  };

  return {
    handleResetGame,
    setupGame,
    restartGame,
    items,
    setItems,
    incrementMovements,
    handleDragItems,
  };
};
