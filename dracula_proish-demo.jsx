function Slayer(props) {
  return <h1>{props.name}</h1>;
}

// Comment
function DraculaPro() {
  return (
    <div>
      <Slayer name="Blade" />
      <Slayer name="Buffy" />
      <Slayer name="Lincoln" />
      <Slayer name="Morbius" />
      <Slayer name="Van Helsing" />
    </div>
  );
}

ReactDOM.render(
  <DraculaPro />,
  document.getElementById('root')
);
