import * as THREE from 'three';
/**
 *	地板
 */
const Field = function(){
  const _this = this;
  const WIDTH = 10;
	/**
	 *	初始化
	 */
	_this.init = () => {
    THREE.Object3D.call(_this);
    for (let m = 0; m < 4; m++) {
      for (let n = 0; n < 4; n++) {
        const color = (m + n) % 2 == 0 ? 0xff0000:0x0000ff;
        const cube = createTile(color);
        cube.position.x = m * WIDTH;
        cube.position.y = n * WIDTH;
        _this.add(cube );
      }
    }
  };
  /**
   * 生成瓦片
   */
  function createTile(color) {
    const geometry = new THREE.BoxGeometry(WIDTH, WIDTH, 1);
    const material = new THREE.MeshBasicMaterial( { color } );
    const cube = new THREE.Mesh( geometry, material );
    return cube;
  }
	_this.init();
};

Field.prototype = Object.create( THREE.Object3D.prototype );
Field.prototype.constructor = Field;
export default Field;