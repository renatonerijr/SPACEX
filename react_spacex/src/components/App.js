import React from 'react';
import '../style/App.css';

class App extends React.Component {


        constructor(props){
            super(props)
            this.state = {
                info: null,
                flight_number: 0,
                is_upcoming: false
            }

        }

        fetchFromAPI(slug){
            const url = 'http://127.0.0.1:8000/launches/'+slug;
            fetch(url, {method: 'GET', contenttypes: 'application/json'})
                .then(response => response.json())
                .then(jsonResponse => {
                    console.log(jsonResponse)
                    this.setState({
                        info: jsonResponse,
                        flight_number: jsonResponse.flight_number
                    })
                })
                .catch(err => {
                    console.log(err)
                })
        }

        componentDidMount() {
            this.fetchFromAPI('latest')
        }


        render() {
            return (
                <div className="container-fluid">
                    { this.state.info &&
                    <div className="row">

                        <div className="col-4 stages">

                                <h1>Mission Name</h1>
                                <p>{this.state.info.mission_name}</p>

                                <h1>Launch Year</h1>
                                <p>{this.state.info.launch_year}</p>

                                <h1>Launch Date</h1>
                                <p>{this.state.info.launch_date_utc}</p>

                                <h1>Details</h1>
                                <p className="details">{this.state.info.details}</p>

                                <h1>Reused?</h1>
                                {this.state.info.launch_success != null ?
                                    <p>{this.state.info.rocket.first_stage.is_reused ? "Yes" : "No" }</p>
                                    :
                                    <p>N/A</p>
                                }

                                <h1>Land Success</h1>
                                {this.state.info.launch_success != null ?
                                    <p>{this.state.info.launch_success ? "Yes" : "No" }</p>
                                    :
                                    <p>N/A</p>
                                }

                                <h1>Landing Intent</h1>
                                {this.state.info.launch_success != null ?
                                    <p>{this.state.info.rocket.first_stage.landing_intent ? "Yes" : "No" }</p>
                                    :
                                    <p>N/A</p>
                                }

                        </div>

                        <div className="col stages">

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
                                <input type="number" value={this.state.flight_number}/>
                            </div>
                        </div>

                        <div className="col mission-report">
                            <div>
                                <h1>Rocket</h1>
                                <p>{this.state.info.rocket.first_stage.rocket_name}</p>
                            </div>
                            <img className="rocket-img" src={this.state.info.imgs[0]} alt="Rocket"/>
                            <img className="mission-patch" src={this.state.info.img_mission_patch} alt="Patch"/>
                            <div>
                                <h1>Launch Site</h1>
                                <p>{this.state.info.launch_site}</p>
                            </div>
                            <div>
                                <a href="last" style={{ textDecoration: !this.state.is_upcoming ? 'underline' : 'none' }} >
                                    Last Missions
                                </a>
                                <span> | </span>
                                <a href="next" style={{ textDecoration: this.state.is_upcoming ? 'underline' : 'none' }}>
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
