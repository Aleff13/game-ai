import {useState} from 'react';
import {IItem} from '../interfaces/item.interface';

export const useBeatGame = () => {
  const [beatSteps, setBeatSteps] = useState<Array<Array<number>>>();
  const [inputs, setInputs] = useState([]);
  const [outputs, setOutputs] = useState([]);

  const handleResetBeatSteps = () => setBeatSteps([]);

  const handleBeatSteps = (items: IItem[]) => {
    const newStep = items.map(item => item.value);

    const sameArr = (arr1: any[], arr2: string | any[]) => {
      if (arr1.length !== arr2.length) {
        return false;
      }
      return arr1.every((element, index) => element === arr2[index]);
    };

    const filteredBeatSteps = beatSteps?.filter(
      (element, index, self) =>
        index === self.findIndex(elem => sameArr(elem, element)),
    );

    if (!filteredBeatSteps) {
      setBeatSteps([newStep]);
      return;
    }

    setBeatSteps([...filteredBeatSteps, newStep]);
  };

  const displayBeatSteps = () => {
    const filteredBeatSteps = [...new Set(beatSteps), [1, 2, 3, 4, 5, 6]];
    const copiedBeatSteps = filteredBeatSteps.slice();
    copiedBeatSteps.pop();
    setInputs([...inputs, ...copiedBeatSteps])
    console.log('-------BEGIN------');

    console.log('input', inputs);

    filteredBeatSteps.shift();
    setOutputs([...outputs, ...filteredBeatSteps]);
    console.log('output', outputs);
    console.log('-------FINISH------');
  };

  return {handleResetBeatSteps, handleBeatSteps, displayBeatSteps};
};
