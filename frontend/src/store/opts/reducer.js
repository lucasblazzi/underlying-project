import { GET_OPTION } from "./actionTypes";

const INIT_STATE = {
    data: [],
}

const option = (state = INIT_STATE, action) => {
    switch (action.type) {
        case GET_OPTION:
            return {
                ...state,
                data: action.payload,
            }

        default:
            return state
    }
}

export default option