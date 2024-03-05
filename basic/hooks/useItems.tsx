/* eslint-disable @typescript-eslint/no-shadow */
import {useState} from 'react';
import {IItem} from '../interfaces/item.interface';

export const useItems = () => {
  const [movements, setMovements] = useState(0);

  const [items, setItems] = useState<IItem[]>([
    {
      key: '1',
      value: 3,
      width: 170,
      backgroundColor: '#37b580',
      margin: 25,
    },
    // {
    //   key: '2',
    //   value: 4,
    //   width: 200,
    //   backgroundColor: '#2ec6b7',
    //   margin: 10,
    // },
    // {
    //   key: '3',
    //   value: 6,
    //   width: 240,
    //   backgroundColor: '#453c9a',
    //   margin: 0,
    // },
    {
      key: '4',
      value: 2,
      width: 130,
      backgroundColor: '#f80000',
      margin: 42,
    },
    {
      key: '5',
      value: 1,
      width: 100,
      backgroundColor: '#121212',
      margin: 53,
    },
    // {
    //   key: '6',
    //   value: 5,
    //   width: 220,
    //   backgroundColor: '#c4d767',
    //   margin: 0,
    // },
  ]);

  const shuffleItems = (items: IItem[]) => {
    const ref = [...items];
    let shuffledItems = ref?.sort(() => Math.random() - 0.5);

    while (isAsc(shuffledItems)) {
      shuffledItems = ref?.sort(() => Math.random() - 0.5);
    }

    setItems(shuffledItems);
  };

  const isAsc = (items: IItem[]) => {
    return items.every((x, i) => {
      return i === 0 || x.value >= items[i - 1].value;
    });
  };

  const resetMovementsCounter = () => {
    setMovements(0);
  };

  const incrementMovements = () => {
    setMovements(movements + 1);
  };

  const handleDragItems = (data: IItem[]) => {
    setItems(data);
    incrementMovements();
  };

  return {
    items,
    setItems,
    shuffleItems,
    isAsc,
    movements,
    resetMovementsCounter,
    incrementMovements,
    handleDragItems,
  };
};
