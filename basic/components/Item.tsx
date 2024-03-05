import React from 'react';
import {
  GestureResponderEvent,
  StyleSheet,
  TouchableOpacity,
  View,
} from 'react-native';
import {
  useOnCellActiveAnimation,
  ScaleDecorator,
  OpacityDecorator,
  ShadowDecorator,
} from 'react-native-draggable-flatlist';
import {IItem} from '../interfaces/item.interface';

interface RenderItemProps {
  item: IItem;
  drag?: ((event: GestureResponderEvent) => void) | undefined;
}

export const Item = ({item, drag}: RenderItemProps) => {
  const {isActive} = useOnCellActiveAnimation();

  return (
    <View accessibilityLabel={`item-${item.value}`}>
      <ScaleDecorator>
        <OpacityDecorator activeOpacity={0.5}>
          <ShadowDecorator>
            <TouchableOpacity
              onLongPress={drag}
              activeOpacity={1}
              style={[
                styles.rowItem,
                // eslint-disable-next-line react-native/no-inline-styles
                {
                  height: 50,
                  width: item.width,
                  backgroundColor: item.backgroundColor,
                  elevation: isActive ? 30 : 0,
                  // marginLeft: item.margin,
                },
              ]}
            />
          </ShadowDecorator>
        </OpacityDecorator>
      </ScaleDecorator>
    </View>
  );
};

const styles = StyleSheet.create({
  rowItem: {
    alignContent: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    borderRadius: 50,
  },
});
