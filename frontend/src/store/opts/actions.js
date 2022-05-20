import {
    GET_OPTION
} from './actionTypes';

export const getOption = optData => ({
    type: GET_OPTION,
    payload: optData,
})