import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

    constructor(props){
        super(props)
        this.state = {
            latest: {},
            next: {},
            upcoming: [],
            past: []
        }

    }
    componentDidMount() {
      this.fecthLatest();
    }

    async fecthLatest(){
        const url = 'http://127.0.0.1:8000/launches/latest';
        const response = await fetch(url, {method: 'GET', contenttypes: 'application/json'});
        const json = await response.json()
        console.log(json)
    }

    render() {
        return (
            <h1>Hello World!  </h1>
        );
    }
}

export default App;
