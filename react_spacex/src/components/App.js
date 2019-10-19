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
            this.handleLatest = this.handleLatest.bind(this)
            this.handleNext = this.handleNext.bind(this)
            this.handleInput = this.handleInput.bind(this)
            this.handleInputClickUp = this.handleInputClickUp.bind(this)
            this.handleInputClickDown = this.handleInputClickDown.bind(this)

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

        handleNext(e) {
            e.preventDefault();
            this.fetchFromAPI('next')
            this.setState({is_upcoming: true})
        }

        handleLatest(e) {
            e.preventDefault();
            this.fetchFromAPI('latest')
            this.setState({is_upcoming: false})
        }

        handleInput(event) {
            let num = parseInt(event.target.value)
            if(isNaN(num)){
                return
            }
            this.fetchFromAPI(num)
        }

        handleInputClickUp(){
            this.setState(prevState => {
                return {
                    flight_number: prevState.flight_number + 1,
                    info: prevState.info,
                    is_upcoming: prevState.is_upcoming
                }
            })
            this.fetchFromAPI(this.state.flight_number+1)

        }

        handleInputClickDown(){
            this.setState(prevState => {
                return {
                    flight_number: prevState.flight_number - 1
                }
            })
            this.fetchFromAPI(this.state.flight_number-1)
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

                            <div className="flight_div">
                                <h1>Flight Number</h1>
                                <div className="flight_selector">
                                    <i className="fas fa-chevron-up" onClick={this.handleInputClickUp}></i>
                                    <input value={this.state.flight_number} onChange={this.handleInput}/>
                                    <i className="fas fa-chevron-down" onClick={this.handleInputClickDown}></i>
                                </div>
                            </div>
                        </div>

                        <div className="col mission-report">

                            <div>
                                <h1>Rocket</h1>
                                <p>{this.state.info.rocket.first_stage.rocket_name}</p>
                            </div>

                            <img
                                className="rocket-img"
                                src={this.state.info.imgs[0] ? this.state.info.imgs[0] : "https://via.placeholder.com/1000?text=N/A"}
                                alt="Rocket"
                            />
                            <img
                                className="mission-patch"
                                src={this.state.info.img_mission_patch ? this.state.info.img_mission_patch : "https://via.placeholder.com/1000?text=N/A"}
                                alt="Patch"
                            />

                            <div>
                                <h1>Launch Site</h1>
                                <p>{this.state.info.launch_site}</p>
                            </div>
                            <div>
                                <a
                                    href="last"
                                    style={{ textDecoration: !this.state.is_upcoming ? 'underline' : 'none' }}
                                    onClick={this.handleLatest}
                                 >
                                    Last Mission
                                </a>
                                <span> | </span>
                                <a
                                    href="next"
                                    style={{ textDecoration: this.state.is_upcoming ? 'underline' : 'none' }}
                                    onClick={this.handleNext}
                                >
                                    Next Mission
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
