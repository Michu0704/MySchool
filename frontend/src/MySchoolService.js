import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class MySchoolService{

    constructor(){}


    getCatalogs() {
        const url = `${API_URL}/api/catalogs/`;
        return axios.get(url).then(response => response.data);
    }
    getCatalogsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
}