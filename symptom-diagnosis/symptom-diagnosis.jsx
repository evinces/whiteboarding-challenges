// Symptom Diagnosis

// Design and implement a sypmtom intake and diagnosis form

// +-------------------------------------------+
// | +----------------+-------------+--------+ |
// | | Enter Symptoms | _textField_ | Search | |
// | +----------------+-------------+--------+ |
// | | Discovered search terms from ML model | |
// | +---------------------------------------+ |
// |                                           |
// | +---------------------------------------+ |
// | | Diagnosis                             | |
// | | Description                           | |
// | +---------------------------------------+ |
// | | Diagnosis                             | |
// | | Description                           | |
// | +---------------------------------------+ |
// | | ...                                   | |
// | +---------------------------------------+ |
// +-------------------------------------------+


class SymptomForm extends React.Component {
  constructor(props) {
    super(props);
    this.textEl = null;
  }

  getDiagnoses = () => {
    fetch("/get-diagnoses", {
      method: "post",
      header: new Header({
        contentType: "application/json"
      }),
      body: JSON.stringify({
        query: this.textEl.value
      })
    })
    .then(r => r.json())
    .then(this.props.callback(r));
  }

  render() {
    return (
      <form onSubmit={this.getDiagnoses}>
        <label htmlFor="symptomText">
          Enter Symptoms
        </label>
        <input id="symptomText" type="text" ref={el => this.textEl = el} />
        <button type="submit">
          Search
        </button>
      </form>
    );
  }
}
