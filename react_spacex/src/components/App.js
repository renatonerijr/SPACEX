import React from 'react';
import '../style/App.css';

class App extends React.Component {


        constructor(props){
            super(props)
            this.state = {
                info: null,
            }

        }

        fetchLatest(){
            const url = 'http://127.0.0.1:8000/launches/next';
            fetch(url, {method: 'GET', contenttypes: 'application/json'})
                .then(response => response.json())
                .then(jsonResponse => {
                    console.log(jsonResponse)
                    this.setState({info: jsonResponse})
                })
                .catch(err => {
                    console.log(err)
                })
        }

        componentDidMount() {
            this.fetchLatest()
        }


        render() {
            return (
                <div>
                    { this.state.info &&
                    <div>
                        <div>
                            <h1>Mission Name</h1>
                            <p>{this.state.info.mission_name}</p>
                        </div>

                        <div>
                            <h1>Launch Year</h1>
                            <p>{this.state.info.launch_year}</p>
                        </div>

                        <div>
                            <h1>Launch Date</h1>
                            <p>{this.state.info.launch_date_utc}</p>
                        </div>


                        <div>
                            <h1>Details</h1>
                            <p>{this.state.info.details}</p>
                        </div>


                        <div>
                            <h1>Reused?</h1>
                            {this.state.info.launch_success != null ?
                                <p>{this.state.info.rocket.first_stage.is_reused ? "Yes" : "No" }</p>
                                :
                                <p>N/A</p>
                            }
                        </div>


                        <div>
                            <h1>Land Success</h1>
                            {this.state.info.launch_success != null ?
                                <p>{this.state.info.launch_success ? "Yes" : "No" }</p>
                                :
                                <p>N/A</p>
                            }
                        </div>


                        <div>
                            <h1>Landing Intent</h1>
                            {this.state.info.launch_success != null ?
                                <p>{this.state.info.rocket.first_stage.landing_intent ? "Yes" : "No" }</p>
                                :
                                <p>N/A</p>
                            }
                        </div>

                        <div>
                            <h1>Costumers</h1>
                            <p>{this.state.info.rocket.second_stage.costumers.join(", ")}</p>
                        </div>

                        <div>
                            <h1>Manufacturer</h1>
                            <p>{this.state.info.rocket.second_stage.manufacturer}</p>
                        </div>

                        <div>
                            <h1>Nationality</h1>
                            <p>{this.state.info.rocket.second_stage.nationality}</p>
                        </div>

                        <div>
                            <h1>Launch Success</h1>
                            {this.state.info.launch_success != null ?
                                <p>{this.state.info.launch_success ? "Yes" : "No"}</p>
                                :
                                <p>N/A</p>
                            }
                        </div>

                        <div>
                            <h1>Flight Number</h1>
                            <button>aa</button>
                            <input/>
                            <button>aa</button>
                        </div>

                        <div>
                            <div>
                                <h1>Rocket</h1>
                                <p>{this.state.info.rocket.first_stage.rocket_name}</p>
                            </div>
                            <img src="" />
                            <img src="" />
                            <div>
                                <h1>Launch Site</h1>
                                <p>{this.state.info.launch_site}</p>
                            </div>
                            <div>
                                <a href="#">
                                    Last Missions
                                </a>
                                <a href="#">
                                    Next Missions
                                </a>
                            </div>
                        </div>

                    </div>
                    }





                </div>
            );
        }
}

export default App;
