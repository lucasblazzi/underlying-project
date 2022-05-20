import { call, put, takeEvery } from "redux-saga/effects"

import { GET_OPTION } from "./actionTypes"

import { getOption } from "./actions"
import { post } from "helpers/api_helper"

async function opt(url) {
    return await post(url, null)
}

function* fetchOption() {
    try {
        const response = yield put(opt('https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/search'))
        console.log('!! Resposta !!\n' + response)
    } catch (error) {
        console.log('!! ERRO !!\n' + error)
    }
}

// watchers
function* optsSaga() {
    yield takeEvery(GET_OPTION, fetchOption)
}

export default optsSaga