import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from "@app/store";

// Define a type for the slice state
interface CounterState {
    value: number
}

// Define the initial state using that type
const initialState = {
    value: 0,
} as CounterState

export const counterSlice = createSlice({
    name: 'counter',
    initialState,
    reducers: {
        increment: state => {
            // Redux Toolkit allows us to write "mutating" logic in reducers. It
            // doesn't actually mutate the state because it uses the immer library,
            // which detects changes to a "draft state" and produces a brand new
            // immutable state based off those changes
            state.value += 1;
        },
        decrement: state => {
            state.value -= 1;
        },
        incrementByAmount: (state, action: PayloadAction<number>) => {
            state.value += action.payload;
        }
    }
})

// thunk
export const selectCount = (state: RootState) => state.counter.value

export const {increment, decrement, incrementByAmount} = counterSlice.actions;

export default counterSlice.reducer;
