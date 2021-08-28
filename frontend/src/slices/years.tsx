import { createSlice, createAsyncThunk, PayloadAction, Draft } from '@reduxjs/toolkit';
import { RootState } from "@app/store";
import cartographer from "@common/cartographer.api";

type Status = 'IDLE' | 'LOADING' | 'FAILED' | 'SUCCEEDED';

interface YearsState {
    list: Array<string | undefined>,
    status: Status
}

// Define the initial state using that type
const initialState = {
    list: [],
    status: 'IDLE'
} as YearsState

// Async thunks

export const initialise = createAsyncThunk('years/initialise', async () => {
    const resp = await cartographer('GET', 'years');
    return resp.data.years;
})

export const yearsSlice = createSlice({
    name: 'years',
    initialState,
    reducers: {
        set: (state: Draft<YearsState>, action: PayloadAction<[]>) => {
            state.list = action.payload;
        },
        initialiseYears: state => {
            cartographer('GET', 'years')
                .then(value => {
                    state.list = value.data.years;
                    console.log(value);
                })
                .catch(err => console.log(err));
        }
    },
    extraReducers: (builder) => {
        builder.addCase(initialise.pending, (state, action) => {
            state.status = 'LOADING';
        });
        builder.addCase(initialise.fulfilled, (state, action) => {
            state.status = 'SUCCEEDED';
            // Add any fetched posts to the array
            state.list = action.payload;
        });
        builder.addCase(initialise.rejected, (state, action) => {
            state.status = 'FAILED';
        });
    }
})

// thunk
export const selectYear = (state: RootState) => state.years.list;

export const {set} = yearsSlice.actions;

export default yearsSlice.reducer;
