import axios from '@/libs/api.request'

// 定义了一个api
export const login = (email, password) => {
    return axios.request({
        url: 'user/login/',
        data: {
            email: email,
            password: password
        },
        method: 'post'
    })
}

export const register = (name, email, password) => {
    return axios.request({
        url: 'user/register/',
        data: {
            email: email,
            password: password,
            name: name
        },
        method: 'post'
    })
}
// 验证token
export const check_token = (token) => {
    return axios.request({
        url: 'user/check_token/',
        params: {
            token: token
        },
        method: 'get'
    })
}

// 向后端请求MFtoken
export const get_MFtoken = () => {
    return axios.request({
        url: 'user/get_MFtoken',
        method: 'get'
    })
}
