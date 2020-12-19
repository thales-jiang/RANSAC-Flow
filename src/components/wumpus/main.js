import * as THREE from 'three';
import Field from './field';
/**
 *	版本
 */
const VER = "1.0";
/**
 *	事件
 */
const EVENT = {
	RUNNING:	"running",
	MODEL_LOADED:	"modeLoaded",
	PERSON_FAIL: "personFail",
	GAME_INIT: "gameInit",
	GAME_START:	"gameStart",
	GAME_OVER:	"gameOver"
};
const main = function(container){
	const _this = this;
	
	let WIDTH = 0,
		HEIGHT = 0;
		
	let __camera = null,	//摄像头
		__scene = null,	//场景
		__renderer = null,	//渲染器
		__field = null;	//场地
	var _clock = new THREE.Clock();
	var __stats = null;	//fps
	/**
	 *	初始化
	 */
	_this.init = function(container) {
    // console.log(container.attributes);
		WIDTH = 500;
		HEIGHT = 500;
    __scene = new THREE.Scene();
    __camera = new THREE.PerspectiveCamera( 75, WIDTH / HEIGHT, 1, 1000 );
    __camera.position.z = 100;
    __renderer = new THREE.WebGLRenderer({canvas: container});
    __renderer.setSize( WIDTH, HEIGHT );

    __field = new Field();
    __scene.add( __field );
    animate();
  };
  _this.start = () => {
    console.log("start");
  };
  function animate() {
    requestAnimationFrame( animate );
    __field.rotation.x += 0.01;
    __field.rotation.y += 0.01;
    __renderer.render( __scene, __camera );
  }
	_this.init(container);
};

Object.assign( main.prototype, THREE.EventDispatcher.prototype);
main.prototype.constructor = main;
export {main,VER,EVENT};