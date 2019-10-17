import React from 'react';

class ComponentTest extends React.Component {

    constructor(props){
        super(props)
        this.state = {
            latest: null,
            next: null,
            upcoming: null,
            past: null
        }

    }
    componentDidMount() {
      this.fetchLatest();
      this.fetchNext();
      this.fetchUpcoming();
      this.fetchPast();
    }

    fetchLatest(){
        const url = 'http://127.0.0.1:8000/launches/latest';
        fetch(url, {method: 'GET', contenttypes: 'application/json'})
            .then(response => response.json())
            .then(jsonResponse => {
                this.setState({latest: jsonResponse})
                console.log(jsonResponse)
            })
            .catch(err => {
                console.log(err)
            })
    }

    fetchNext(){
        const url = 'http://127.0.0.1:8000/launches/next';
        fetch(url, {method: 'GET', contenttypes: 'application/json'})
            .then(response => response.json())
            .then(jsonResponse => {
                this.setState({next: jsonResponse})
            })
            .catch(err => {
                console.log(err)
            })
    }

    fetchUpcoming(){
        const url = 'http://127.0.0.1:8000/launches/upcoming';
        fetch(url, {method: 'GET', contenttypes: 'application/json'})
            .then(response => response.json())
            .then(jsonResponse => {
                this.setState({upcoming: jsonResponse})
            })
            .catch(err => {
                console.log(err)
            })
    }

    fetchPast(){
        const url = 'http://127.0.0.1:8000/launches/past';
        fetch(url, {method: 'GET', contenttypes: 'application/json'})
            .then(response => response.json())
            .then(jsonResponse => {
                this.setState({past: jsonResponse})
            })
            .catch(err => {
                console.log(err)
            })
    }


    render() {
        return (
            <div>
                <h1>Teste</h1>
             </div>
        );
    }
}

export default ComponentTest;
